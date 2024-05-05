import React from 'react';

const rooms = (props) => {
  
    return (
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
                            <a className="btn btn-outline-dark mt-auto" href="/preview">Xem phòng</a>
                          </div>                                 
                      </div>
                    </div>
                  </div>                   

                )
            })}
        
      </div>
    );
};

export default rooms;