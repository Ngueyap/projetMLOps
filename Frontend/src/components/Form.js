import React, { useState } from "react";

import axios from 'axios';

const Form = () => {
  const [formValue, setFormValue] = useState({
    title : "",
    genre : "",
    description : "",
    type : "",
    producer : "",
    studio : "",
  }); 
  
  const [prediction, setPrediction] = useState("");

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormValue((prevState) => {
      return {
        ...prevState,
        [name]: value,
      };
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Envoyer les données du formulaire au backend ici
    // exemple avec axios
    axios.post('http://127.0.0.1:5000/api/anime', formValue)
      .then(res => {
        console.log(res.data);
        setPrediction(res.data.prediction); // Mettre à jour l'état avec la prédiction renvoyée par le backend
      })
      .catch(err => {
        console.error(err);
      });
  };
  
  const { title, genre, description, type, producer, studio} = formValue;
  return (
  <div>
    <h2>Prediction: {prediction}</h2> 
    <form onSubmit={handleSubmit}>
     <label>
        Anime Title:
        <input
          name="title"
          type="text"
          value={title}
          onChange={handleChange} />
      </label>
      <br />
      <label>
        Anime Genres:
        <input
          name="genre"
          type="text"
          value={genre}
          onChange={handleChange} />
      </label>
      <br />
      <label>
        Anime Description:
        <input
          name="description"
          type="text"
          value={description}
          onChange={handleChange} />
      </label>
      <br />
      <label>
        Anime Type:
        <input
          name="type"
          type="text"
          value={type}
          onChange={handleChange} />
      </label>
      <br />
      <label>
        Anime Producer:
        <input
          name="producer"
          type="text"
          value={producer}
          onChange={handleChange} />
      </label>
      <br />
      <label>
        Anime Studio:
        <input
          name="studio"
          type="text"
          value={studio}
          onChange={handleChange} />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  </div>
  );
};

export default Form;
