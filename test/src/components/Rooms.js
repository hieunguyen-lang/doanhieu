import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import Xemphong from '../pages/Xemphong.js';
const Rooms = (props) => {
   
    const sort = (sort) =>{
      props.setFilters({
        ...props.filters,
        sort
      });
    };
    const address = (address) =>{
      props.setFilters({
        ...props.filters,
        address
      });
    };
    const [roomid, setRoomid] = useState([]);
    const handleButtonClick = (value) => {
      // Lấy giá trị của button khi click
      setRoomid(value);
      console.log(setRoomid)
    };
    let button;
    button = (
      <div className="d-flex justify-content-center" style={{ backgroundColor: '#FDF4E5', fontFamily: 'Mulish, sans-serif' }}>
        <button type="button" class="btn ">Xem thêm</button>
      </div>
    )
    return (
      <> 
      
        <div className='col-md-3 mb-4 input-group' style={{ height: '300px'}}>
          <div>
            </div>
            <div className="col">  
                    <h5> Lọc theo giá</h5>    
                    <select  className="form-control text-center  form-outline-dark" onChange={e => sort(e.target.value)}>
                            
                        <option value="asc">Giá thấp nhất trước</option>
                        <option value="desc">Giá cao nhất trước</option>
                        

                    </select>
              </div> 
            <div className="col">  
                    <h5>Khu vực</h5>    
                    <select  className="form-control text-center  form-outline-dark" onChange={e => address(e.target.value)}>
                            
                        <option value=""> Tất cả khu vực</option> 
                        <option value="Hoàn Kiếm"> Hoàn Kiếm</option>
                        <option value="Ba Đình"> Ba Đình</option>
                        <option value="Tây Hồ"> Tây Hồ</option>
                        <option value="Hai Bà Trưng"> Hai Bà Trưng</option>
                        <option value="Đống Đa"> Đống Đa</option>
                        <option value="Thanh Xuân Cầu Giấy"> T.Xuân- C.Giấy</option>   


                    </select>
              </div> 
        </div>
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            {props.rooms.map(room=> {
                return(
   
                <div className="col">
                    <div className="card shadow-sm">
                        <img src={`http://localhost:8000/${room.Hinhanh}`} height={500}/>
                      <div className="card-body">
                        <h3 className="fw-bolder"> {room.Ten} </h3>
                        <h5 className="">Giá Từ: {room.Gia4tieng} </h5>
                        <h6>Địa chỉ {room.Diachi}</h6>
                        
                          <div className="text-center">
                            <a href={`http://localhost:8000/preview/${room.id}`} className="btn btn-outline-dark mt-auto" onClick={() => handleButtonClick(room.id)} >Xem phòng</a>
                         
                          </div>                                 
                      </div>
                    </div>
                  </div>                   

                )
            })}   

      </div>
      
      {button}
      <Xemphong roomid={roomid} />
      </>
    );
};

export default Rooms;