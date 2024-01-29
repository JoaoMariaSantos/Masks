import React, {useContext} from 'react'
import ProxyContext from '../ProxyContext';

function StickersDownload() {
    const proxyUrl = useContext(ProxyContext)

    const downloadStickers = () => {
        fetch(proxyUrl + '/downloadStickers')
          .then((response) => response.blob())
          .then((blob) => {
            const url = window.URL.createObjectURL(new Blob([blob]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'IncognitoStickers.pdf');  // Update with the desired file name
            document.body.appendChild(link);
            link.click();
          })
          .catch((error) => {
            console.error('Error downloading PDF:', error);
          });
      };



  return (
    <button id='stickersDownloadButton' className="cell" onClick={downloadStickers}>
        Download Sticker Set
    </button>
  )
}

export default StickersDownload;