import React, {useState, useEffect} from 'react'
import Banner from './Banner'
import Header from './Header'
import HelpButton from './HelpButton'

function InputPage() {
  const [imageIndex, setImageIndex] = useState(0);
  const images = ['/explanation/explanation_0.png', '/explanation/explanation_1.png'];

  useEffect(() => {
    const intervalId = setInterval(() => {
      setImageIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 2000);

    return () => clearInterval(intervalId); // Cleanup the interval on component unmount

  }, [imageIndex, images.length]);

  const handleGetStartedButton = () => {
    const element = document.getElementById('inputPage');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div id='introductionPage' className='page'>
      <div>
        {/*<Banner/>
        <Header/>
        <HelpButton/>*/}
        <div id='introduction_explanation' className='cell'>
          <div id='introduction_explanation-message'>Facial recognition software won't know it's you!</div>
          <div id='introduction_explanation-gif'>
            <img src={images[imageIndex]} alt={`Image ${imageIndex + 1}`} />
          </div>
          <div id='introduction_explanation-code'>
          <a href="https://github.com/JoaoMariaSantos/Masks" className='cell' target="_blank" id='codeButton'>
            <span>
                See the Code
            </span>
          </a>
          </div>
        </div>
        <div id='introduction_guide' className='cell'>
          <div id='introduction_steps'>
            <div>1. Show us a photo of yourself;</div>
            <div>2. Select some emojis;</div>
            <div>3. Generate your sticker set;</div>
            <div>4. Download and print your stickers;</div>
            <div>5. Apply the stickers to your face;</div>
            <div>6. Stay incognito!</div>
          </div>

          <div id='introduction_getStarted'>
            <button className='cell'  onClick={handleGetStartedButton}><span>Get Started</span></button>
          </div>
        </div>


      </div>
    </div>
  )
}

export default InputPage