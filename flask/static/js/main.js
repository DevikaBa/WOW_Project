// toggle the menu bar on the home page
const menuToggle = document.querySelector('.toggle')
const showcase = document.querySelector('.showcase')

menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active')
    showcase.classList.toggle('active')
})

var changeFont = function() {
    $("container h4.colorFont").css("display", "none")
}
changeFont()






