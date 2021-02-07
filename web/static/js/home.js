"use strict";

// --- CONSTANTS ---
const SECTION_Y_OFFSET = 150;


// import {} from "/static/js/validateFormHelpers"
/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("sideBar").classList.add("expanded", "shadow-lg");
    document.getElementById("overlay").classList.add("active");
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("sideBar").classList.remove("expanded", "shadow-lg");
    document.getElementById("overlay").classList.remove("active");
}

function addListeners(element, listener, ...eventNames) {
    for (let i = 0, iLen = eventNames.length; i < iLen; i++) {
        element.addEventListener(eventNames[i], listener, false);
    }
}

function ajaxGetJSON(url, callback) {
    let request = new XMLHttpRequest();
    request.open('GET', url, true);

    request.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status >= 200 && this.status < 400) {
                // Success!
                const data = JSON.parse(this.responseText);
                callback(data);
            } else {
                // Error :(
            }
        }
    };

    request.send();
    request = null;
}

function ajaxPostJSON(url, json, onSuccess, onError) {
    console.log(json);
    const request = new XMLHttpRequest();
    // Define what happens on successful data submission
    request.addEventListener("load", event => {
        // alert(event.target.responseText);
        console.log(event.target);
        onSuccess(event);
    });

    // Define what happens in case of error
    request.addEventListener("error", event => {
        console.log("Failed to post data", event);
        onError(event);
    });
    request.open('POST', url, true);
    request.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    request.send(json);
}


function getPicsumUrl(id, width, height) {
    return `https://picsum.photos/id/${id}/${width}/${height}`;
}


function initFeedbackForm() {
    const form = document.getElementById("feedbackForm");
    const submitButton = form.querySelector("#sendFeedback");

    const validateContacts = form => {
        let result = true;
        if (!form.elements.email.value && !form.elements.phone.value) {
            showErrorsForInput(form.elements.email, null, true);
            showErrorsForInput(form.elements.phone, "Пожалуйста, укажите хотя бы один способ связи");
            result = false;
        } else {
            showErrorsForInput(form.elements.email, null);
            showErrorsForInput(form.elements.phone, null);
        }
        return result;
    };

    const postData = () => {
        let formDataObj = Object.fromEntries(new FormData(form));

        ajaxPostJSON("/api/feedback-requests/", JSON.stringify(formDataObj),
            ev => {
                alert("Запрос отправлен успешно! Мы свяжемся с Вами в ближайшее время.");
            },
            ev => {
                alert("Что-т пошло не так! Пожалуйста, повторите попытку чуть позже.");
            }
        );
    };

    const handleFeedbackSubmit = ev => {
        if (!validateContacts(form)) return;

        // validate the form against the constraints
        const errors = validate(form, constraints);
        // then we update the form to reflect the results
        showErrors(form, errors || {});
        if (!errors) {
            postData();
        } else {
            console.error("Failed", errors);
        }
    };

    form.addEventListener("submit", ev => {
        ev.preventDefault();
        handleFeedbackSubmit(ev);
    });

    const constraints = {
        email: {
            // presence: {
            //     allowEmpty: false,
            //     message: "Пожалуйста, введите адрес электронной почты"
            // },
            // email: true
            email: {
                message: "введён некорректно"
            }
        },
        phone: {
            // presence: {
            //     allowEmpty: false
            // },
            format: {
                pattern: "^(\\+)?7\\d{10,11}$",
                message: "Неверный формат номера телефона. Прим.: +78004919067"
            }
        },
        theme: {
            // presence: true
        },
        message: {
            // presence: true
        }
    };

    const inputs = form.querySelectorAll("input, textarea, select");
    forEach(inputs, input => {
        input.addEventListener("change", () => {
            if (!validateContacts(form)) return;
            const errors = validate(form, constraints) || {};
            showErrorsForInput(input, errors[input.name]);
        });
    });

    const phoneInput = form.querySelector("input#phone");
    phoneInput.addEventListener("change", evt => {
        console.log("Phone: ", evt);
        phoneInput.value = phoneInput.value.replaceAll(/[^0-9+]/g, "");
    });

}

function initSmoothSectionScrolls() {
//  little hack to detect if the user is on ie 11
    const isIE11 = !!window.MSInputMethodContext && !!document.documentMode;
    // get all the links with an ID that starts with 'sectionLink'
    const listOfLinks = document.querySelectorAll("a[href^='#']");
    // loop over all the links
    listOfLinks.forEach(function (link) {
        // listen for a click
        link.addEventListener('click', (ev) => {
            ev.preventDefault();

            let ref = link.hash;
            // ref = "#section" + ref[1];
            // ie 11 does not support smooth scroll, so we will simply scroll
            if (isIE11) {
                window.scrollTo(0, document.querySelector(ref).offsetTop - 50);
            } else {
                window.scroll({
                    behavior: 'smooth',
                    left: 0,
                    // top gets the distance from the top of the page of our target element
                    top: document.querySelector(ref).offsetTop - 50
                });
            }
        });
    });
}

function initScrollListeners() {
    const sections = document.querySelectorAll("[data-nav]");
    console.log(sections);

    class NavNode {
        /**
         *
         * @param {HTMLAnchorElement[]} anchors
         * @param {HTMLElement} section
         */
        constructor(anchors, section) {
            this.navAnchors = anchors;
            this.section = section;
        }

        activate() {
            this.navAnchors.forEach((anchor) => {
                anchor.classList.add("active");
            });
        }

        deactivate() {
            this.navAnchors.forEach((anchor) => {
                anchor.classList.remove("active");
            });
        }

        /**
         * @param {NavNode} other
         * @returns {boolean}
         */
        equals(other) {
            return other && (this === other || (this.navAnchors === other.navAnchors && this.section === other.section));
        }
    }

    /** @type {NavNode[]} */
    let navNodes = [];
    forEach(sections, (section) => {
        navNodes.push(new NavNode(
            Array.from(document.querySelectorAll(`a[href='#${section.id}']`)),
            section
        ));
    });

    /** @type {NavNode} */
    let lastActiveNav = null;

    /**
     * @param {NavNode} navNode
     */
    const setActiveSection = (navNode) => {
        if (navNode.equals(lastActiveNav)) return;

        if (lastActiveNav) {
            lastActiveNav.deactivate();
        }

        navNode.activate();
        lastActiveNav = navNode;
    };

    const navbar = document.querySelector("#navbar");
    const checkScroll = () => {
        // Navbar scrolled style
        const navAtTop = navbar.offsetHeight / 2; //The point where the navbar changes in px
        if (window.scrollY > navAtTop) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }

        // Current nav section highlight
        let target = 0;
        for (let i = 0; i < navNodes.length; i++) {
            if (window.scrollY >= navNodes[i].section.offsetTop - SECTION_Y_OFFSET) {
                target = i;
            } else if (i !== navNodes.length - 1) {
                setActiveSection(navNodes[target]);
                return;
            }
        }

        setActiveSection(navNodes[target]);
    };

    addListeners(window,
        () => {
            checkScroll();
        },
        "scroll", "resize");
    checkScroll();
}


function initGallery() {
    // Create and mount the thumbnails slider.
    const thumbnailSlider = new Splide('#thumbnailSlider', {
        rewind: true,
        fixedWidth: 100,
        fixedHeight: 64,
        isNavigation: true,
        gap: 10,
        focus: 'center',
        pagination: false,
        cover: true,
        // lazyLoad: 'sequential',
        breakpoints: {
            '600': {
                fixedWidth: 66,
                fixedHeight: 40,
            }
        }
    }).mount();

    // Create the main slider.
    const primarySlider = new Splide('#primarySlider', {
        type: 'fade',
        heightRatio: 0.5,
        pagination: false,
        arrows: false,
        cover: true,
        // lazyLoad: 'nearby',
    });

    // Set the thumbnails slider as a sync target and then call mount.
    primarySlider.sync(thumbnailSlider).mount();

    const renderPrimaryItem = (id, imageUrl, description) => {
        return (`
        <li class="splide__slide">
            <a href="${imageUrl}" target="_blank" rel="noopener noreferrer">
                <img src="${imageUrl}" alt="${id} ${description}">
            </a>
        </li>
        `).trim();
    };

    const {protocol, host} = window.location;
    ajaxGetJSON(`${protocol}//${host}/api/gallery/`, data => {
        for (const i in data) {
            const {id, image, description} = data[i];
            primarySlider.add(renderPrimaryItem(id, image, description));
            thumbnailSlider.add(`<li class="splide__slide"><img src="${image}" alt="${id} ${description}"></li>`);
        }
    });
}


// Runs when DOM is ready
const start = () => {
    AOS.init();

    initSmoothSectionScrolls();

    // initScrollListeners();

    initScrollListeners();

    initGallery();

    initFeedbackForm();
};


if (document.readyState !== 'loading') {
    start();
} else {
    document.addEventListener('DOMContentLoaded', start);
}
