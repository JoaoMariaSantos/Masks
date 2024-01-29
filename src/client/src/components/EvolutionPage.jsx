import React, {useState, useEffect, useContext} from 'react'
import EvolutionCell from './EvolutionCell'
import IndividualCell from './IndividualCell'
import Banner from './Banner'
import ProxyContext from '../ProxyContext';

function EvolutionPage() {
  const proxyUrl = useContext(ProxyContext)

  const [loadIndividual, setLoadIndividual] = useState(false);
  const [bestFitness, setBestFitness] = useState(0);
  const [individualSrc, setIndividualSrc] = useState(null);

  useEffect(() => {
    const intervalId = setInterval(() => {
        setLoadIndividual(true);
    }, 4000);

    return () => clearInterval(intervalId);

  }, [loadIndividual]);

  useEffect(() => {
    if (!loadIndividual) {
      return;
    }

    fetch(proxyUrl + "/bestIndividual") //fetching best individual image
      .then((res) => res.blob())
      .then((blob) => {
        //console.log(blob);
        if (blob["type"].includes("image")) {
          const individualUrl = URL.createObjectURL(blob);
          setIndividualSrc(individualUrl);
          //console.log(individualUrl);
        } else {
          setIndividualSrc(null);
        }
      })
      .catch((error) => console.error("Image not available:", error));
      setLoadIndividual(false);

    fetch(proxyUrl + "/bestFitness", { //fetching best individual fitness
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.json())
    .then(data => {
      setBestFitness(data.value[0]);
    })
    .catch(error => {
      console.error('Error fetching fitness:', error);
    });
  }, [loadIndividual]);



  return (
    <div id='evolutionPage' className='page'>
      <div>
        <Banner/>
        <EvolutionCell bestFitness={bestFitness}/>
        <IndividualCell individualSrc={individualSrc} bestFitness={bestFitness}/>
      </div>
    </div>
  )
}

export default EvolutionPage