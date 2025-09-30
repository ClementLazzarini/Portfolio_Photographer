// Obtenez la liste des images du diaporama
const slide = document.querySelector('.home1-slide');
const images = slide.querySelectorAll('img');

// Obtenez les flèches gauche et droite
const arrowLeft = document.querySelector('.arrow-l');
const arrowRight = document.querySelector('.arrow-r');

// Variables pour le défilement
let currentIndex = 0;
const intervalTime = 3600; // Temps en millisecondes entre chaque défilement
let slideInterval;

// Fonction pour mettre à jour le compteur d'images
const updateImageCounter = () => {
    const imageCounter = document.getElementById('image-counter');
    const currentImageIndex = currentIndex + 1;
    const totalImages = images.length;
    imageCounter.textContent = `${String(currentImageIndex).padStart(2, '0')}/${String(totalImages).padStart(2, '0')}`;
};

// Fonction pour faire défiler vers la gauche
const slideLeft = () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlidePosition();
    updateImageCounter(); // Mettre à jour le compteur d'images
};

// Fonction pour faire défiler vers la droite
const slideRight = () => {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlidePosition();
    updateImageCounter(); // Mettre à jour le compteur d'images
};

// Met à jour la position du diaporama
const updateSlidePosition = () => {
    const offset = -currentIndex * 100;
    slide.style.transform = `translateX(${offset}%)`;
};

// Gestionnaire d'événements pour les flèches
arrowLeft.addEventListener('click', slideLeft);
arrowRight.addEventListener('click', slideRight);

// Fonction pour déclencher le défilement automatique
const startSlideShow = () => {
    slideInterval = setInterval(slideRight, intervalTime);
};

// Fonction pour arrêter le défilement automatique
const stopSlideShow = () => {
    clearInterval(slideInterval);
};

// Démarrer le défilement automatique au chargement de la page
startSlideShow();
updateImageCounter();

// Gestionnaires d'événements pour arrêter/démarrer le défilement automatique au survol
slide.addEventListener('mouseover', stopSlideShow);
slide.addEventListener('mouseout', startSlideShow);
