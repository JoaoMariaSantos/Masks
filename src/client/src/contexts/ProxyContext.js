import React, { createContext} from 'react'
export const ProxyContext = createContext()
const ProxyContextProvider = (props) => {
    const ProxyUrl = "http://localhost:5000"
    return (
         <ProxyContext.Provider 
            value={{
                ProxyUrl
             }}>
               {props.children}
         </ProxyContext.Provider>
    )
}
export default ProxyContextProvider