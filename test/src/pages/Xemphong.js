import React, { useEffect, useState } from 'react';
import RoomDetail from '../components/RoomDetail';
import { useParams } from 'react-router-dom/cjs/react-router-dom';

const Xemphong = () => {
  const {id} = useParams();
  const [roomid, setroomid] =useState([]);
 
  useEffect(()=>{
      (
        async() => {
          
          
          const response = await  fetch(`http://localhost:8000/filter?id=${id}`);
          const content = await  response.json();
          setroomid(content.data);
          
        }
      )()
  }, []);
 
    return (
       <div>
       { roomid ?(
         <div class="container px-4 px-lg-5 my-5">
            <div class="row gx-4 gx-lg-5 align-items-center">
                <div class="col-md-6"><img class="card-img-top mb-5 mb-md-0" src={`http://localhost:8000/${roomid.Hinhanh}`} alt="..."></img></div>
                <div class="col-md-6">
                    <div class="small mb-1">SKU: BST-498</div>
                    <h1 class="display-5 fw-bolder">{roomid.Ten}</h1>
                    <div class="fs-5 mb-5">
                        <span class="text-decoration-line-through">$45.00</span>
                        <span>$40.00</span>
                    </div>
                    <p class="lead">Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium at dolorem quidem modi. Nam sequi consequatur obcaecati excepturi alias magni, accusamus eius blanditiis delectus ipsam minima ea iste laborum vero?</p>
                    <div class="d-flex">
                        <input class="form-control text-center me-3" id="inputQuantity" type="num" value="1" style={{maxwidth: "3rem"}}></input>
                        <button class="btn btn-outline-dark flex-shrink-0" type="button">
                            <i class="bi-cart-fill me-1"></i>
                            Add to cart
                        </button>
                    </div>
                </div>
            </div>
        </div>
        ) : (
            <p>Loading...</p>
        )}
       </div>
    );
};

export default Xemphong;