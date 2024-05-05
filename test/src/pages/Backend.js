import React, { useEffect, useState } from 'react';
import Rooms from '../components/Rooms';

const Backend = () => {
    const [rooms, setRooms] = useState([] );
     useEffect(()=>{
        (
          async() => {
            const response = await fetch('http://http://127.0.0.1:8000/filter');
            const content = await response.json();
            setRooms(content);
          }
        )()
    }, []);
    return (
       <Rooms rooms={rooms}/>
    );
};

export default Backend;