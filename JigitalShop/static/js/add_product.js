document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".add-product-form");
    const rateInput = document.getElementById("id_rate");
    const priceInput = document.getElementById("id_price");
    const photoInput = document.getElementById("id_photo");

    form.addEventListener("submit", function (event) {
        // Перевірка рейтингу
        const rateValue = parseFloat(rateInput.value);
        if (rateValue < 1.0 || rateValue > 5.0) {
            event.preventDefault();
            alert("Рейтинг має бути в межах від 1.0 до 5.0!");
            rateInput.focus();
            return;
        }

        // Перевірка ціни
        const priceValue = parseFloat(priceInput.value);
        if (priceValue <= 0 || isNaN(priceValue)) {
            event.preventDefault();
            alert("Ціна має бути позитивним числом!");
            priceInput.focus();
            return;
        }

        // Перевірка наявності фото
        if (!photoInput.files.length) {
            event.preventDefault();
            alert("Будь ласка, завантажте фото продукту!");
            photoInput.focus();
            return;
        }
    });
});
