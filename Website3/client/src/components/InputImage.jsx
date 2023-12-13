import React, { useState, useContext } from 'react';
import ProxyContext from '../ProxyContext';

function InputImage({notifyUpload}) {
  const proxyUrl = useContext(ProxyContext)

  const handleUpload = async (e) => {
    const file = e.target.files[0];

    if (file != null) {
      const formData = new FormData();
      formData.append('face', file);
  
      fetch(proxyUrl + '/uploadface',
        {
          method: 'post',
          body: formData,
        }
      ).then(response => response.json())
      .then(data => {
        console.log(data);
        notifyUpload(data['error'][0]);
      })
      .catch(error => console.error('ERROR:', error));
    }
  };

  return (
    <div id="photos_upload">
          <input id="photos_upload_input" type="file" name="image" accept=".png, .jpg" onChange={handleUpload} className='hidden'/>
          <label id="photos_upload_input_label" htmlFor="photos_upload_input" className='cell'>Upload</label>
    </div>
  )
}

export default InputImage