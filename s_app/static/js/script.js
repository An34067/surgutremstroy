const navbar = document.querySelector('.navbar');
const burger = document.getElementById('burger');
const navLinks = document.getElementById('nav-links');

function updateNavbarOnScroll() {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}

updateNavbarOnScroll();

const currentPath = window.location.pathname;
const links = document.querySelectorAll('.navbar-links a');

links.forEach(function(link) {
    let linkPath = link.getAttribute('href');
    
    if (linkPath === currentPath || 
        (linkPath === '/' && currentPath === '/index/') ||
        (linkPath !== '/' && currentPath.startsWith(linkPath) && linkPath !== '')) {
        link.classList.add('active');
    }
});

burger.addEventListener('click', function() {
    navLinks.classList.toggle('open');
});

window.addEventListener('scroll', updateNavbarOnScroll);


const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
