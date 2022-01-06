const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const fistForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const signin_container = document.querySelector(".signin_container");

signInBtn.addEventListener("click", () => {
    signin_container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
    signin_container.classList.add("right-panel-active");
});

fistForm.addEventListener("submit", (e) => e.preventDefault());
secondForm.addEventListener("submit", (e) => e.preventDefault());