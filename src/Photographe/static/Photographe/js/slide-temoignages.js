// Obtenez la liste des cartes témoignages
const testimonialsSlide = document.querySelector('.home3-slide');
const testimonialCards = testimonialsSlide.querySelectorAll('.home3-card');

// Obtenez les flèches gauche et droite pour les témoignages
const arrowLeftTestimonials = document.querySelector('.arrow-l3');
const arrowRightTestimonials = document.querySelector('.arrow-r3');

// Variables pour le défilement des témoignages
let currentTestimonialIndex = 0;
const intervalTimeTestimonials = 5000; // Temps en millisecondes entre chaque défilement des témoignages
let testimonialsInterval;

// Fonction pour faire défiler les témoignages vers la gauche
const slideLeftTestimonials = () => {
    currentTestimonialIndex = (currentTestimonialIndex - 1 + testimonialCards.length) % testimonialCards.length;
    updateTestimonialsSlidePosition();
};

// Fonction pour faire défiler les témoignages vers la droite
const slideRightTestimonials = () => {
    currentTestimonialIndex = (currentTestimonialIndex + 1) % testimonialCards.length;
    updateTestimonialsSlidePosition();
};

// Met à jour la position du diaporama de témoignages
const updateTestimonialsSlidePosition = () => {
    const offset = -currentTestimonialIndex * 100;
    testimonialsSlide.style.transform = `translateX(${offset}%)`;
};

// Gestionnaire d'événements pour les flèches de témoignages
arrowLeftTestimonials.addEventListener('click', slideLeftTestimonials);
arrowRightTestimonials.addEventListener('click', slideRightTestimonials);

// Fonction pour déclencher le défilement automatique des témoignages
const startTestimonialsSlideShow = () => {
    testimonialsInterval = setInterval(slideRightTestimonials, intervalTimeTestimonials);
};

// Fonction pour arrêter le défilement automatique des témoignages
const stopTestimonialsSlideShow = () => {
    clearInterval(testimonialsInterval);
};

// Démarrer le défilement automatique des témoignages au chargement de la page
startTestimonialsSlideShow();

// Gestionnaires d'événements pour arrêter/démarrer le défilement automatique des témoignages au survol
testimonialsSlide.addEventListener('mouseover', stopTestimonialsSlideShow);
testimonialsSlide.addEventListener('mouseout', startTestimonialsSlideShow);
