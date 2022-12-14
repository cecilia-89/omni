//Module: main.js resposible for site responsive


//displays search when user clicks on it
let ul = document.querySelector('[data-list]')

document.querySelector('.fa-magnifying-glass').addEventListener(
    'click', () => {
        document.querySelector('[data-search]').classList.toggle('visible')
        document.querySelector('.logo').classList.toggle('none')
        ul.classList.add('hide')
    })

//returns movie title that includes user input
document.querySelector(
    '[data-search]').addEventListener('input', (e) => {

        value = (e.target.value.toLowerCase())
        let spaces = value.trim().length
        ul.classList.remove('hide')

        if (spaces === 0) {
            ul.classList.add('hide')
        }

        while (ul.firstChild) {
            ul.removeChild(ul.firstChild)
        }

        movies.forEach(movie => {
            let title = movie.title.toLowerCase()

            if (title.includes(value)){
                let li = document.createElement('li')
                li.textContent = movie.title
                ul.append(li)
            } else {
                ul.style.border = '0'
            }
        })
    })

//fetch api that gets data from the url provided

let movies = []
fetch('/search').then(
    (response) =>
    response.json()).then(
        (data) =>
        movies = data.map(item => {
            return {title: item.title}
        })
    )


let start = 0;
let end = 0;

//detects finger swipe direction and
//scrolls div to the left or right

document.querySelectorAll('.slider').forEach(slide => {
    slide.addEventListener('touchstart', (e) => {
        start = e.changedTouches[0].screenX;
        console.log(e.changedTouches)
        console.log(start)
    })

    slide.addEventListener('touchend', (e) => {
        end = e.changedTouches[0].screenX;
        console.log(end)
        checkDir(slide)
    })

    slide.addEventListener('touchmove', (e) => {
        slide.scrollBy(50, 0)
    })

})


function checkDir(param) {
    if (end < start) param.scrollBy(900, 0)
    if (end > start) param.scrollBy(-900, 0)
  }


// simple query to enable div scroll left
//or right based on the arrow direction

document.querySelectorAll('[data-arrow]').forEach(arrow => {

    arrow.addEventListener('click', () => {
        if (arrow.dataset.arrow === 'right') {
            let prev = arrow.previousElementSibling
            prev.scrollBy(900, 0)
        } else {
            let next = arrow.nextElementSibling
            next.scrollBy(-900, 0)
        }
    })
})



//detects finger movement and moves to either
//previous or next element sibling

let slides = document.querySelector('[data-slides]');
let touchstartX = 0;
let touchendX = 0;

slides.addEventListener('touchstart', (e) => {
    touchstartX = e.changedTouches[0].screenX
})

slides.addEventListener('touchend', (e) => {
  touchendX = e.changedTouches[0].screenX
  checkDirection()
})

function checkDirection() {
    if (touchendX < touchstartX) swipe (1)
    if (touchendX > touchstartX) swipe(-1)
  }


//moves to the previous or next element sibling
//based on the arrow direction

let item = document.querySelector('.recent_movie')
item.classList.add('data-image')

document.querySelectorAll('[data-angle]').forEach(arrow => {

    arrow.addEventListener('click', () => {
        let count = arrow.dataset.angle === 'next' ? 1:-1;
        swipe(count)
    })
})


//enables a user to swipe left or right
let swipe = (count) => {
    var currentImage = slides.querySelector('.data-image')
    var nextIndex = [...slides.children].indexOf(currentImage) + count
    var currentIndex =  [...slides.children].indexOf(currentImage)
    if(nextIndex < 0) nextIndex= [...slides.children].length -1
    if(nextIndex >= [...slides.children].length) nextIndex = 0
    slides.children[nextIndex].classList.add('data-image')
    slides.children[currentIndex].classList.remove('data-image')
}