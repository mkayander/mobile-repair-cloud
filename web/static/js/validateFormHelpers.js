"use strict";

const isString = obj => {
    return (Object.prototype.toString.call(obj) === '[object String]');
};

// Simple forEach loop that should work in IE browsers too
const forEach = (list, fn) => {
    Array.from(list).every(item => {
        fn(item);
        return true;
    });
};

const getCookie = name => {
    let cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');

        for (let i = 0; i < cookies.length; i++) {
            const cookie = jQuery.trim(cookies[i]);

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
};


// Adds the specified error with the following markup
// <p class="help-block error">[message]</p>
const appendError = (msgContainer, error) => {
    const block = document.createElement("p");
    // block.classList.add("help-block");
    block.classList.add("error");
    block.innerText = error;
    msgContainer.appendChild(block);
};


const resetFormGroup = formGroup => {
    // Remove the success and error classes
    formGroup.querySelector(".form-control").classList.remove("is-invalid");
    // and remove any old messages
    forEach(formGroup.querySelectorAll(".messages > .error"), el => {
        el.parentNode.removeChild(el);
    });
};


// Shows the errors for a specific input
const showErrorsForInput = (input, errors, forceInvalid = false) => {
    // This is the root of the input
    // const formGroup = closestParent(input.parentNode, "form-group");
    const formGroup = input.parentNode;
    // Find where the error messages will be insert into
    const msgContainer = formGroup.querySelector(".messages");
    // First we remove any old messages and resets the classes
    resetFormGroup(formGroup);

    if (forceInvalid) {
        input.classList.add("is-invalid");
    }
    // If we have errors
    console.log("Show these errors - ", errors);
    if (errors) {
        // we first mark the group has having errors
        input.classList.add("is-invalid");

        if (isString(errors)) {
            appendError(msgContainer, errors);
        } else {
            // then we append all the errors
            forEach(errors, error => {
                appendError(msgContainer, error);
            });
        }
    }
};


// Updates the inputs with the validation errors
const showErrors = (form, errors) => {
    // We loop through all the inputs and show the errors for that input
    forEach(form.querySelectorAll("input[name], select[name]"), input => {
        // Since the errors can be null if no errors were found we need to handle that
        showErrorsForInput(input, errors && errors[input.name]);
    });
};
