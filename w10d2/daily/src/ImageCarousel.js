import React from "react";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // Import the carousel styles
import hongkong from "./images/hongkong.jpg";
import macao from "./images/macao.webp";
import japan from "./images/japan.webp";
import lasvegas from "./images/lasvegas.webp";

const ImageCarousel = () => {
  return (
    <Carousel showArrows={true} infiniteLoop={true}>
      <div>
        <img src={hongkong} alt="Hong Kong" />
        <p className="legend">Hong Kong</p>
      </div>
      <div>
        <img src={macao} alt="Macao" />
        <p className="legend">Macao</p>
      </div>
      <div>
        <img src={japan} alt="Japan" />
        <p className="legend">Japan</p>
      </div>
      <div>
        <img src={lasvegas} alt="Las Vegas" />
        <p className="legend">Las Vegas</p>
      </div>
    </Carousel>
  );
};

export default ImageCarousel;
