// Daily

class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }

  watch() {
    return `${this.uploader} watched all ${this.time} of ${this.title}!`;
  }
}

const got = new Video("GoT", "Disappointments", 9999);
console.log(got.watch());

const twd = new Video("TwD", "Disappointments 2 electric boogaloo", 9998);
console.log(twd.watch());

const videoData = [
  ["Dancing Show", "DanceStar", 180],
  ["Gardening Tips", "GreenThumb", 480],
  ["Science Experiment", "ScienceLover", 240],
  ["Travel Vlog", "Wanderer", 720],
  ["Music Concert", "MusicFanatic", 900],
];

const videoInstances = [];
for (const data of videoData) {
  const [title, uploader, time] = data;
  const video = new Video(title, uploader, time);
  videoInstances.push(video);
}

for (const video of videoInstances) {
  console.log(video.watch());
}
