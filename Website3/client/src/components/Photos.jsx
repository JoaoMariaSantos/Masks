import React, { useState, useEffect, useContext } from "react";
import InputImage from "./InputImage";
import ProxyContext from "../ProxyContext";

function Photos({ notifyPhotoChange }) {
  const proxyUrl = useContext(ProxyContext);

  const [uploadedFaceSrc, setUploadedFaceSrc] = useState(null);
  const [errorFace, setErrorFace] = useState("");
  const [loadFace, setLoadFace] = useState(false);

  const inputCellClasses = () => {
    let classes = "cell inputCell";
    if (uploadedFaceSrc) classes += " inputCell_ready";
    return classes;
  };

  //gets the face photo URL after being notified of upload
  useEffect(() => {
    if (loadFace) {
      fetch(proxyUrl + "/uploadedface")
        .then((res) => res.blob())
        .then((blob) => {
          console.log(blob);
          if (blob["type"].includes("image")) {
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
  const handleUploadNotification = (error) => {
    console.log(error);
    setErrorFace(error);

    const goodPhoto = error === "";

    setLoadFace(goodPhoto);
    notifyPhotoChange(goodPhoto);
    if (!goodPhoto) setUploadedFaceSrc(null);
  };

  return (
    <div id="photos">
      <div className={inputCellClasses()}>
        <div className="inputCell_heading">
          <h2>Photo</h2>
        </div>
        <div className="inputCell_description">
          <p>Upload a photo of yourself facing foward so that it won't be recognized</p>
        </div>
         {/*<div className="inputCell_assurance">
          <p>It is only used for the generation</p>
        </div>*/}
        <div className="inputCell_input">
          <InputImage notifyUpload={handleUploadNotification} />
        </div>
        <div className="inputCell_result">
          <div id="uploadedPhotos">
            {uploadedFaceSrc && (
              <img src={uploadedFaceSrc} alt="uploaded photo" />
            )}
            {errorFace !== "" && <span>{errorFace}</span>}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Photos;
