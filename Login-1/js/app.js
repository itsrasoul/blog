// Get elements
const loginTab = document.getElementById('login-tab');
const registerTab = document.getElementById('register-tab');
const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');
const body = document.body;

// Function to show login form and hide register form with animations
function showLoginForm() {
    loginForm.classList.add('active');
    registerForm.classList.remove('active');
    loginTab.classList.add('active');
    registerTab.classList.remove('active');

    // Add animation effect
    loginForm.style.animation = "slideIn 0.7s ease-in-out forwards";
    registerForm.style.animation = "fadeOut 0.5s ease-in-out forwards";
    
    // Change background
    body.classList.add('background-login');
    body.classList.remove('background-register');
}

// Function to show register form and hide login form with animations
function showRegisterForm() {
    registerForm.classList.add('active');
    loginForm.classList.remove('active');
    registerTab.classList.add('active');
    loginTab.classList.remove('active');

    // Add animation effect
    registerForm.style.animation = "slideIn 0.7s ease-in-out forwards";
    loginForm.style.animation = "fadeOut 0.5s ease-in-out forwards";
    
    // Change background
    body.classList.add('background-register');
    body.classList.remove('background-login');
}

// Event listeners for tab buttons
loginTab.addEventListener('click', showLoginForm);
registerTab.addEventListener('click', showRegisterForm);

// Initially show the login form
showLoginForm();
