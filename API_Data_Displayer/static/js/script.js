// Turn IN_TRANSIT into "IN TRANSIT" for display (used on the output page)
// document.querySelectorAll(".fmt").forEach(function (el) {
//     el.textContent = el.textContent.replace(/_/g, " ");
// });

// // Search form logic (only runs on the input page)
// (function () {
//     var form = document.getElementById("trackForm");
//     if (!form) return;   // not on the input page, so do nothing

//     var input = document.getElementById("shipmentNum");
//     var btn = document.getElementById("submitBtn");
//     var btnText = document.getElementById("btnText");

//     // Clicking an example chip fills the input
//     document.querySelectorAll(".chip").forEach(function (chip) {
//         chip.addEventListener("click", function () {
//             input.value = chip.getAttribute("data-value");
//             input.focus();
//         });
//     });

//     // Clean the value and show a loading state while the API call runs
//     form.addEventListener("submit", function () {
//         input.value = input.value.trim().toUpperCase();
//         btn.classList.add("loading");
//         btn.disabled = true;
//         btnText.textContent = "Fetching details…";
//     });

//     // Reset the button if the user comes back with the browser's back button
//     window.addEventListener("pageshow", function () {
//         btn.classList.remove("loading");
//         btn.disabled = false;
//         btnText.textContent = "Track Shipment";
//     });
// })();
// Turn IN_TRANSIT into "IN TRANSIT" for display (used on the output page)
document.querySelectorAll(".fmt").forEach(function (el) {
    el.textContent = el.textContent.replace(/_/g, " ");
});

// Search form logic (only runs on the input page)
(function () {
    var form = document.getElementById("trackForm");
    if (!form) return;   // not on the input page, so do nothing

    var input = document.getElementById("shipmentNum");
    var btn = document.getElementById("submitBtn");
    var btnText = document.getElementById("btnText");

    // Clicking an example chip fills the input
    document.querySelectorAll(".chip").forEach(function (chip) {
        chip.addEventListener("click", function () {
            input.value = chip.getAttribute("data-value");
            input.focus();
        });
    });

    // Clean the value and show a loading state while the API call runs
    form.addEventListener("submit", function () {
        input.value = input.value.trim().toUpperCase();
        btn.classList.add("loading");
        btn.disabled = true;
        btnText.textContent = "Fetching details…";
    });

    // Reset the button if the user comes back with the browser's back button
    window.addEventListener("pageshow", function () {
        btn.classList.remove("loading");
        btn.disabled = false;
        btnText.textContent = "Track Shipment";
    });
})();