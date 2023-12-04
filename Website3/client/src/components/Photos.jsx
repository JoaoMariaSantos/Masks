import React, { useState, useEffect } from "react";
import InputImage from "./InputImage";

function Photos({notifyPhotoChange}) {
  const [uploadedFaceSrc, setUploadedFaceSrc] = useState(null);
  const [errorFace, setErrorFace] = useState("");
  const [loadFace, setLoadFace] = useState(false);

  //gets the face photo URL after being notified of upload
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
            notifyPhotoChange(false);
          }
        })
        .catch((error) => console.error("Image not available:", error));
      setLoadFace(false);
    }
  }, [loadFace]);

  //to be notified by child InputImage when photo is uploaded
  const handleUploadNotification = (error) =>{
    console.log(error);
    setErrorFace(error);

    const goodPhoto = error === "";

    setLoadFace(goodPhoto);
    notifyPhotoChange(goodPhoto);
    if(!goodPhoto) setUploadedFaceSrc(null);
  }


  return (
    <div id="photos" >
      <div className="cell inputCell">
        <div className="inputCell_heading">
          <h2>Photo</h2>
        </div>
        <div className="inputCell_description">
          <p>Upload a photo of yourself facing foward</p>
        </div>
        <div className="inputCell_assurance">
          <p>It will only be used to for the generation</p>
        </div>
        <div className="inputCell_input">

          <InputImage notifyUpload={handleUploadNotification}/>
          
        </div>
        <div className="inputCell_result">

          <div id="uploadedPhotos">
            {uploadedFaceSrc && <img src={uploadedFaceSrc} alt="uploaded photo"/>}
            {errorFace !== "" && <span>{errorFace}</span>}
          </div>

        </div>
      </div>
    </div>
  );
}

export default Photos;
