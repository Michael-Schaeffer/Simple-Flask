function clickBurger() {
    let x = document.getElementById("flex_nav");
    if (x.className === "flex-container") {
        x.className += " responsive";
    } else {
        x.className = "flex-container";
    }
}
