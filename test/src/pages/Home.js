import React, { useEffect, useLayoutEffect, useState } from 'react';
import Rooms from '../components/Rooms';
import { wait } from '@testing-library/user-event/dist/utils';

const Home = () => {
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
       <Rooms rooms={rooms}/>
    );
};

export default Home;