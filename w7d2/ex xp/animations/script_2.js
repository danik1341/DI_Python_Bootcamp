let intervalId;
const animateBox = document.getElementById('animate');
const container = document.getElementById('container');

const myMove = () => {
    let positon = 0;

    intervalId = setInterval(() => {
        if (positon >=container.offsetWidth - animateBox.offsetWidth){
            clearInterval(intervalId);
        } else {
            positon++;
            animateBox.style.left = positon + 'px';
        }
    }, 1)
}

myMove();