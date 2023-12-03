import React, {useState, useEffect} from 'react'

function App() {

  const [data, setData] = useState ([{}])

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
    <div>
      <h1>yo</h1>
    </div>
  )
}

export default App;