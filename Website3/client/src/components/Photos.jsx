import React, { useState, useEffect } from "react";
import InputImage from "./InputImage";

function Photos() {
  const [uploadedFaceSrc, setUploadedFaceSrc] = useState(null);
  const [loadFace, setLoadFace] = useState(true);

  useEffect(() => {
    if(loadFace){
      fetch("/uploadedface")
        .then((res) => res.blob())
        .then((blob) => {
          console.log(blob)
          if(blob['type'].includes('image')){
            const faceUrl = URL.createObjectURL(blob);
            setUploadedFaceSrc(faceUrl);
            console.log(faceUrl);
          } else {
            setUploadedFaceSrc(null);
          }
        })
        .catch((error) => console.error("Image not available:", error));
      setLoadFace(false);
    }
  }, [loadFace]);

  const handleUploadNotification = () =>{
    console.log("photo uploaded")
    setLoadFace(true);
  }


  return (
    <div id="photos" >
      <div className="cell inputCell">
        <div className="inputCell_heading">
          <h2>Photos</h2>
        </div>
        <div className="inputCell_description">
          <p>Upload a photo of yourself facing foward</p>
        </div>
        <div className="inputCell_body">
          <div id="uploadedPhotos">
            {uploadedFaceSrc && <img src={uploadedFaceSrc}/>}
          </div>
        <InputImage notifyUpload={handleUploadNotification}/>
        </div>
      </div>
    </div>
  );
}

export default Photos;
