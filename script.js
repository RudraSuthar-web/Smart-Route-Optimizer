// Intersection Observer for animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1
});

// Observe feature cards
document.querySelectorAll('.feature-card').forEach(card => {
    observer.observe(card);
});

// Observe stats
document.querySelectorAll('.stat').forEach(stat => {
    observer.observe(stat);
});

// Add button click handler
document.querySelector('.btn').addEventListener('click', () => {
    alert('Get started clicked! Add your custom action here.');
});