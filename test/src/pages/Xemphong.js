import React, { useEffect, useState } from 'react';
import RoomDetail from '../components/RoomDetail';

const Xemphong = () => {
    const [rooms, setRooms] = useState([] );
    useEffect(()=>{
        (
          async() => {
            const response = await fetch('http://127.0.0.1:8000/filter');
            const content = await response.json();
            setRooms(content);
          }
        )()
    }, []);
    return (
        < RoomDetail RoomDetail ={rooms}/>
    );
};

export default Xemphong;