import React, {useState, useEffect} from 'react'
import MainPage from './components/MainPage'

import './style/style.css'


function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div><MainPage/></div>
  )
}

export default App