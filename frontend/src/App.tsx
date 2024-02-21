import { useState } from 'react'
import './App.css'
import hab1 from './assets/habitacion1.png'
import hab2 from './assets/habitacion2.png'
import hab3 from './assets/habitacion3.png'

function App() {
  const [selectPerson, setSelectPerson] = useState<boolean[]>([false, false, false]);
  const [selectRoom, setSelectRoom] = useState<boolean>(false);
  const [viewRoom, setViewRoom] = useState<boolean>(false);

  const handleCheckboxChange = (index: number) => {
    setSelectPerson(prevState => {
      const updatedSelection = [...prevState];
      updatedSelection[index] = !updatedSelection[index];
      person();
      return updatedSelection;
    });
  };

  const person = ()=>{
    let name;
    if(selectPerson[0]){
      name = 'Persona 1';
      console.log(name);
    }else if(selectPerson[1]){
      name = 'Persona 2';
      console.log(name);
    }else if(selectPerson[2]){
      name = 'Persona 3';
      console.log(name);
    }
  }
  return(
    <>
      <h1>Seleccione la habitación deseada para realizar la reserva</h1>

      <section className='person'>
        <div>
          <input 
              type='checkbox' 
              checked={selectPerson[0]} 
              onChange={() => handleCheckboxChange(0)} 
              disabled={selectPerson[1] || selectPerson[2]} 
            /> 
            Persona 1

            <input 
              type='checkbox' 
              checked={selectPerson[1]} 
              onChange={() => handleCheckboxChange(1)} 
              disabled={selectPerson[0] || selectPerson[2]} 
            /> 
            Persona 2

            <input 
              type='checkbox' 
              checked={selectPerson[2]} 
              onChange={() => handleCheckboxChange(2)} 
              disabled={selectPerson[0] || selectPerson[1]} 
            /> 
            Persona 3
        </div>
      </section>

      <section className='room'>
        <div>
          <img src={hab1} alt="habitacion 1" />
          <button>Reservar habitación</button>
        </div>
        <div>
          <img src={hab2} alt="habitacion 2" />
          <button>Reservar habitación</button>
        </div>
        <div>
          <img src={hab3} alt="habitacion 3" />
          <button>Reservar habitación</button>
        </div>
      </section>

    </>
  )
}

export { App }
