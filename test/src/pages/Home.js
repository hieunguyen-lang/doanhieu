import React, { useEffect, useState } from 'react';
import Rooms from '../components/Rooms';

const Home = () => {
    const [allRooms, setAllRooms] = useState([] );
    const [filterdrooms, setFilterdrooms] =useState([]);
    const [filters, setFilters] = useState( {
      sort: '',
      address: ''
    });
    
    useEffect(()=>{
        (
          async() => {
            
            
            const response = await  fetch("http://localhost:8000/filter");
            const content = await  response.json();
            setAllRooms(content.data);
            setFilterdrooms(content.data);
          }
        )()
    }, []);

    useEffect( () => {
      let rooms =allRooms.filter(p => p.Diachi.indexOf(filters.address) >= 0);
      //search function
      //let rooms =allRooms.filter(p => p.Diachi.toLowerCase().indexOf(filters.s.toLowerCase()) >= 0 ||
      //p.Ten.toLowerCase().indexOf(filters.s.toLowerCase()) >= 0);
      if(filters.sort ==='asc'|| filters.sort==='desc') {
        rooms.sort((a,b)=>{
          const diff = a.Gia4tieng -b.Gia4tieng;
          if(diff === 0) return 0;
          const sign = Math.abs(diff)/diff;
          return filters.sort === 'asc' ? sign: -sign;
        });
      }
      setFilterdrooms(rooms);
    }, [filters]);
  
    return (
      <div>
       <Rooms rooms={filterdrooms} filters={filters} setFilters={setFilters} />
       
       </div>
    );
};

export default Home;