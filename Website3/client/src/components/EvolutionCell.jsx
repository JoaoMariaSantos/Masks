import React from 'react'
import EvolutionBar from './EvolutionBar'

function EvolutionCell({bestFitness}) {
    return (
        <div id='evolutionCell' className='cell'>
            <h2>Evolving sticker set</h2>

            <span>Using Evolutionary Algorithms, we are generating a unique set of stickers, created just for you!</span>

            <span>You can see the best solution found so far, as well as some other solutions.</span>

            <span>The quality of a solution is determined by how little it resembles the unedited picture you submitted.</span>

            <span>Wait for a bit, and you will have your own unique set of stickers ready!</span>

            <span>Once the solution</span>

            <h4>{bestFitness} / 1</h4>

            <EvolutionBar bestFitness={bestFitness}/>
        </div>
    )
}

export default EvolutionCell