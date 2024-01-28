import React, {useEffect, useState, useContext } from 'react'
import ProxyContext from "../ProxyContext";

function IndividualCell() {
    const proxyUrl = useContext(ProxyContext);

    const [loadIndividual, setLoadIndividual] = useState(false);
    const [individualSrc, setIndividualSrc] = useState(null);

    useEffect(() => {
        const intervalId = setInterval(() => {
            setLoadIndividual(true);
        }, 4000);
    
        return () => clearInterval(intervalId);
    
    }, [loadIndividual]);

    useEffect(() => {
        if (loadIndividual) {
          fetch(proxyUrl + "/bestIndividual")
            .then((res) => res.blob())
            .then((blob) => {
              console.log(blob);
              if (blob["type"].includes("image")) {
                const individualUrl = URL.createObjectURL(blob);
                setIndividualSrc(individualUrl);
                console.log(individualUrl);
              } else {
                setIndividualSrc(null);
              }
            })
            .catch((error) => console.error("Image not available:", error));
            setLoadIndividual(false);
        }
      }, [loadIndividual]);


    return (
        <div id='IndividualCell' className='cell'>
            {individualSrc && (
              <img src={individualSrc} alt="best result so far" />
            )}
        </div>
    )
}

export default IndividualCell