function scrolll() {
	let left = document.querySelector('#drama')
	left.scrollBy(350, 0)
}

function scrollr() {
	let right = document.querySelector('#drama')
	right.scrollBy(-350, 0)
}


document.querySelectorAll('.slide-arrow').forEach(arrow => {

    arrow.addEventListener('click', () => {

        let count = arrow.dataset.angle === 'next' ? 1:-1

        let slides = document.querySelectorAll('.recent_movie')

        let currentImage = document.querySelector('[data-image]')

        let nextIndex = Array.from(slides).indexOf(currentImage) + count

        const currentIndex =  Array.from(slides).indexOf(currentImage)

        if(nextIndex < 0) nextIndex= Array.from(slides).length -1

        if(nextIndex >= slides.length) nextIndex = 0

        Array.from(slides)[nextIndex].dataset.image = true

        Array.from(slides)[currentIndex].dataset.images = true

        delete currentImage.dataset.image

    })})
