import React, { useEffect, useState } from 'react';
const Xemphong = ({roomid}) => {
  const [roomdetail, setRoomdetail] = useState([]);
  useEffect(()=>{
      ( 
        async() => {
          
          const roomidNumber = parseInt(roomid, 10);
          const response = await  fetch(`http://localhost:8000/filter/roomid?id=${roomidNumber}`);
          const content = await  response.json();
        
          setRoomdetail(content.data);
        }
      )()
  }, [roomid]);
 
    return (
      
       <div>
        { roomdetail  &&(
         <div className="container px-4 px-lg-5 my-5">
            <div className="row gx-4 gx-lg-5 align-items-center">
                <div className="col-md-6"><img className="card-img-top mb-5 mb-md-0" src={`http://localhost:8000/${roomdetail.Hinhanh}`} alt="..."></img></div>
                <div className="col-md-6">
                    <div className="small mb-1">SKU: BST-498</div>
                    <h1 className="display-5 fw-bolder">{roomdetail.Ten}</h1>
                    <h1 className="display-5 fw-bolder">{roomdetail.Diachi}</h1>
                    <div className="fs-5 mb-5">
                        <span className="text-decoration-line-through">$45.00</span>
                        <span>$40.00</span>
                    </div>
                    <p className="lead">Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium at dolorem quidem modi. Nam sequi consequatur obcaecati excepturi alias magni, accusamus eius blanditiis delectus ipsam minima ea iste laborum vero?</p>
                    <div className="d-flex">
                        <input className="form-control text-center me-3" id="inputQuantity" type="num" value="1" style={{maxwidth: "3rem"}}></input>
                        <button className="btn btn-outline-dark flex-shrink-0" type="button">
                            <i className="bi-cart-fill me-1"></i>
                            Add to cart
                        </button>
                    </div>
                </div>
            </div>
        </div>
        )}
       </div>
    );
};

export default Xemphong;