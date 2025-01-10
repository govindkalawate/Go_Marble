document.getElementById('fetch-reviews').addEventListener('click', async () => {
    const url = document.getElementById('url').value;
    const response = await fetch(`/api/reviews?url=${encodeURIComponent(url)}`);
    const reviews = await response.json();
    const reviewsContainer = document.getElementById('reviews-container');
    reviewsContainer.innerHTML = '';

    if (reviews.length === 0) {
        reviewsContainer.innerHTML = '<p>No reviews found.</p>';
        return;
    }

    reviews.forEach(review => {
        const reviewDiv = document.createElement('div');
        reviewDiv.classList.add('review');
        reviewDiv.innerHTML = `
            <h3>${review.title}</h3>
            <p>${review.body}</p>
            <p>Rating: ${review.rating}</p>
            <p>Reviewer: ${review.reviewer}</p>
            <hr>
        `;
        reviewsContainer.appendChild(reviewDiv);
    });
});