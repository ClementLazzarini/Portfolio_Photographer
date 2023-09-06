import { enableBodyScroll, disableBodyScroll } from './body-scroll-lock.js'

class Lightbox {

    static init () {
        const links = Array.from(document.querySelectorAll('a[href$=".png"], a[href$=".jpg"], a[href$=".jpeg"], a[href$=".mov"], a[href$=".mp4"]'))
        const gallery = links.map(link => link.getAttribute('href'))
        links.forEach(link => link.addEventListener('click', e => {
            e.preventDefault()
            new Lightbox(e.currentTarget.getAttribute('href'), gallery)
        }))
    }

    constructor (url, mediaFiles) {
        this.element = this.buildDOM()
        this.mediaFiles = mediaFiles
        this.currentIndex = mediaFiles.indexOf(url)
        this.loadMedia(url)
        this.onKeyUp = this.onKeyUp.bind(this)
        document.body.appendChild(this.element)
        disableBodyScroll(this.element)
        document.addEventListener('keyup', this.onKeyUp)
    }

    loadMedia (url) {
        const container = this.element.querySelector('.lightbox__container')
        container.innerHTML = ''

        if (url.endsWith('.mov')|| url.endsWith('.mp4')) {
            const video = document.createElement('video')
            video.src = url
            video.controls = true
            container.appendChild(video)
        } else {
            const image = new Image()
            const loader = document.createElement('div')
            loader.classList.add('lightbox__loader')
            container.appendChild(loader)
            image.onload = () => {
                container.removeChild(loader)
                container.appendChild(image)
            }
            image.src = url
        }
    }

    onKeyUp (e) {
        if (e.key === 'Escape'){
            this.close(e)
        } else if (e.key === 'ArrowLeft'){
            this.prev(e)
        } else if (e.key === 'ArrowRight'){
            this.next(e)
        }
    }

    close (e) {
        e.preventDefault()
        this.element.classList.add('fadeOut')
        window.setTimeout(() => {
            this.element.parentElement.removeChild(this.element)
        }, 500)
        enableBodyScroll(this.element)
        document.removeEventListener('keyup', this.onKeyUp)
    }

    next (e) {
        e.preventDefault()
        this.currentIndex = (this.currentIndex + 1) % this.mediaFiles.length
        this.loadMedia(this.mediaFiles[this.currentIndex])
    }

    prev (e) {
        e.preventDefault()
        this.currentIndex = (this.currentIndex - 1 + this.mediaFiles.length) % this.mediaFiles.length
        this.loadMedia(this.mediaFiles[this.currentIndex])
    }

    buildDOM () {
        const dom = document.createElement('div')
        dom.classList.add('lightbox')
        dom.innerHTML = `
            <button class="lightbox__close">Fermer</button>
            <button class="lightbox__next">Suivant</button>
            <button class="lightbox__prev">Précédent</button>
            <div class="lightbox__container">
            </div>`
        dom.querySelector('.lightbox__close').addEventListener('click', this.close.bind(this))
        dom.querySelector('.lightbox__next').addEventListener('click', this.next.bind(this))
        dom.querySelector('.lightbox__prev').addEventListener('click', this.prev.bind(this))
        return dom
    }
}

Lightbox.init()
