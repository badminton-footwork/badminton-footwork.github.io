let wakeLock = null;

function getRandomRedImage() {
    const images = ["data/red_top_left.jpg", "data/red_top_right.jpg", "data/red_bottom_left.jpg", "data/red_bottom_right.jpg", "data/red_left.jpg", "data/red_right.jpg"];
    const randomIndex = Math.floor(Math.random() * images.length);
    return images[randomIndex];
}

function getRandomGreenImage() {
    const images = ["data/green_top_left.jpg", "data/green_top_right.jpg", "data/green_bottom_left.jpg", "data/green_bottom_right.jpg", "data/green_left.jpg", "data/green_right.jpg"];
    const randomIndex = Math.floor(Math.random() * images.length);
    return images[randomIndex];
}

function updateImages() {
    document.getElementById("image1").src = getRandomRedImage();
    document.getElementById("image2").src = getRandomGreenImage();
}

async function requestWakeLock() {
    try {
        wakeLock = await navigator.wakeLock.request('screen');
        wakeLock.addEventListener('release', () => {
            console.log('Screen Wake Lock released:', wakeLock.released);
        });
        console.log('Screen Wake Lock acquired:', wakeLock.released);
    } catch (err) {
        console.error(`${err.name}, ${err.message}`);
    }
}

document.addEventListener('visibilitychange', async () => {
    if (wakeLock !== null && document.visibilityState === 'visible') {
        await requestWakeLock();
    }
});

requestWakeLock();
setInterval(updateImages, 2000);