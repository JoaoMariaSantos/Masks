import React, { useState, useEffect } from 'react';

function HelpButton() {
  const [scrollValue, setScrollValue] = useState(0);
  const [buttonContent, setButtonContent] = useState('!');
  const [buttonTarget, setButtonTarget] = useState('!');

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollValue = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
      setScrollValue(currentScrollValue);

      if (currentScrollValue > 0.5) {
        setButtonContent('?');
        setButtonTarget('introductionPage');
      } else {
        setButtonContent('!');
        setButtonTarget('inputPage');
      }
    };

    window.addEventListener('scroll', handleScroll);

    // Cleanup the event listener when the component is unmounted
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  const handleClickScroll = () => {
    const element = document.getElementById(buttonTarget);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <button id='helpButton' className='cell' onClick={handleClickScroll}><h1>{buttonContent}</h1></button>
  )
}

export default HelpButton