const libForm = document.getElementById('libform');
const libButton = document.getElementById('lib-button');
const storySpan = document.getElementById('story');

const stories = [
    "Once upon a time in a <place>, there lived a <adjective> <noun>. <person> loved to <verb> every day. They were known all over the <place> for their incredible adventures.",
    "In a land far away, <person> discovered a magical <noun>. This <noun> was incredibly <adjective>, and with it, they could <verb> anything they wished. The journey to find the <noun> took them to <place>, a place filled with wonders beyond imagination.",
    "When <person> woke up that morning, they felt unusually <adjective>. Little did they know that <noun> had <verb> during the night. The whole <place> was in chaos as <person> tried to figure out what to do."
];

const generateStory = () =>{
    const nounValue = document.getElementById('noun').value.trim();
    const adjectiveValue = document.getElementById('adjective').value.trim();
    const personValue = document.getElementById('person').value.trim();
    const verbValue = document.getElementById('verb').value.trim();
    const placeValue = document.getElementById('place').value.trim();
    
    if (nounValue === '' || adjectiveValue === '' || personValue === '' || verbValue === '' || placeValue === '') {
        storySpan.textContent = "Please fill in all the inputs.";
        return;
    }
    
    const randomStory = stories[Math.floor(Math.random() * stories.length)];
    
    const story = randomStory
        .replace(/<noun>/g, nounValue)
        .replace(/<adjective>/g, adjectiveValue)
        .replace(/<person>/g, personValue)
        .replace(/<verb>/g, verbValue)
        .replace(/<place>/g, placeValue);
    
    storySpan.textContent = story;
    libButton.textContent = 'Shuffle Stories';
}

libForm.addEventListener('submit', (e) => {
    e.preventDefault();
    generateStory();
})
