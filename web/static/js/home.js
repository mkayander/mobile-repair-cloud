const navbar = document.querySelector(".navbar");
const navbar2 = document.getElementsByClassName("navbar");

function addListeners(element, listener, ...eventNames) {
    for (let i = 0, iLen = eventNames.length; i < iLen; i++) {
        element.addEventListener(eventNames[i], listener, false);
    }
}

function checkScroll() {
    const startY = navbar.offsetHeight / 2; //The point where the navbar changes in px

    if (window.scrollY > startY) {
        // $('.navbar').addClass("scrolled");
        navbar.classList.add("scrolled", "shadow");
    } else {
        // $('.navbar').removeClass("scrolled");
        navbar.classList.remove("scrolled", "shadow");
    }
}

function httpGetJSON(url, callback) {
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

function getPicsumUrl(id, width, height) {
    return `https://picsum.photos/id/${id}/${width}/${height}`;
}


// class FeedbackForm {
//     constructor(email, phone, theme, message) {
//         this.email = email;
//         this.phone = phone;
//         this.theme = theme;
//         this.message = message;
//     }
// }

// function feedbackFormIsValid(data) {
//     if (!data instanceof FeedbackForm) return false;
//
//     let contactValid, emailValid, phoneValid, subjectValid, messageValid;
//     console.log(data);
//
//     contactValid = data.email.value + data.phone.value;
//
//     return contactValid && emailValid && phoneValid && subjectValid && messageValid;
// }

function initFeedbackForm() {
    const form = document.getElementById("feedbackForm");
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
    const handleFeedbackSubmit = ev => {
        if (!validateContacts(form)) return;

        // validate the form against the constraints
        const errors = validate(form, constraints);
        // then we update the form to reflect the results
        showErrors(form, errors || {});
        if (!errors) {
            console.log("Success!", ev);
        } else {
            console.log("Failed", errors);
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
        // phone: {
        //     presence: {
        //         allowEmpty: false
        //     },
        //     format: {
        //         pattern: "^(\\+)?7\\d{10,11}$",
        //         message: "Неверный формат номера телефона. Прим.: +78004919067"
        //     }
        // },
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

    // const feedbackForm = new FeedbackForm(
    //     document.getElementById("email"),
    //     document.getElementById("phone"),
    //     document.getElementById("subject"),
    //     document.getElementById("message")
    // );

    // document.getElementById("sendFeedback").addEventListener("click", ev => {
    //     // console.log(feedbackFormIsValid(feedbackForm));
    //     console.log(validate({
    //         email: feedbackForm.email.value,
    //         phone: feedbackForm.phone.value,
    //         theme: feedbackForm.theme.value,
    //         message: feedbackForm.message.value,
    //     }, constraints));
    // });
}


// Runs when DOM is ready
const start = () => {
    AOS.init();

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

    addListeners(window,
        () => {
            checkScroll();
        },
        "scroll", "resize");
    checkScroll();

    httpGetJSON("https://picsum.photos/v2/list", data => {
        for (const imageId in data) {
            const {id} = data[imageId];
            primarySlider.add(`<li class="splide__slide"><img src="${getPicsumUrl(id, 1110, 555)}" alt="image ${id}"></li>`);
            thumbnailSlider.add(`<li class="splide__slide"><img src="${getPicsumUrl(id, 100, 64)}" alt="image ${id}"></li>`);
        }
    });

    initFeedbackForm();
};


if (document.readyState !== 'loading') {
    start();
} else {
    document.addEventListener('DOMContentLoaded', start);
}
