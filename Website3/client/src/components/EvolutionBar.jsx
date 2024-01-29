import React, {useState, useEffect} from 'react'

function EvolutionBar({bestFitness}) {

    const nCircles = 10;
    const [progressCircles, setProgressCircles] = useState(4); //0-1

    const circlesArray = Array.from({ length: nCircles }, (_, index) => index);

    useEffect(() => {
        setProgressCircles(1 + parseFloat(bestFitness) * nCircles);
        
    }, [bestFitness]);

    return (
        <div id='evolutionBar'>
            {circlesArray.map((index) => (
                    <div key={index} className={index < progressCircles ? 'circle true' : 'circle false'}>
                    </div>
            ))}
        </div>
    )
}

export default EvolutionBar