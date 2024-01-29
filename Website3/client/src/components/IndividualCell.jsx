import React, {useEffect, useState, useContext } from 'react'

function IndividualCell({individualSrc}) {

    return (
        <div id='individualCell' className='cell'>
            {individualSrc && (
              <img src={individualSrc} alt="best result so far" />
            )}
        </div>
    )
}

export default IndividualCell