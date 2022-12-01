document.querySelectorAll('[data-arrow').forEach(arrow => {
    arrow.addEventListener('click', () => {
        let parent = arrow.parentElement
        arrow.dataset.arrow === 'right' ? parent.scrollBy(-350, 0) : parent.scrollBy(350, 0)
    })
})



let item = document.querySelector('.recent_movie')
item.classList.add('data-image')

document.querySelectorAll('.slide-arrow').forEach(arrow => {

    arrow.addEventListener('click', () => {
        let count = arrow.dataset.angle === 'next' ? 1:-1

        var slides = document.querySelector('[data-slides]')

        var currentImage = slides.querySelector('.data-image')


        var nextIndex = [...slides.children].indexOf(currentImage) + count

        var currentIndex =  [...slides.children].indexOf(currentImage)

        if(nextIndex < 0) nextIndex= [...slides.children].length -1

        if(nextIndex >= [...slides.children].length) nextIndex = 0

        slides.children[nextIndex].classList.add('data-image')

        slides.children[currentIndex].classList.remove('data-image')

    })
})
