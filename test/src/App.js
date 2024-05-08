import { BrowserRouter, NavLink, Route } from "react-router-dom";
import Home from "./pages/Home";
import Backend from "./pages/Backend";
import Xemphong from "./pages/Xemphong";
import './App.css'
function App() {
  return (
    <BrowserRouter>
    
      <div class=" "style={{textcolor: 'white'}}>
        <nav className=" navbar navbar-expand-lg sticky-top navbar-dark" style={{ backgroundColor: '#ce3644', fontFamily: 'Mulish, sans-serif' }}>
          <div className="container px-4 px-lg-5 " >              
              <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasExample" aria-controls="offcanvasExample"><i className="bi bi-search"></i></button>
              <NavLink to="/home" className="navbar-brand">LALENDI STUDIO</NavLink>
              <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span className="navbar-toggler-icon "></span></button>
          
              <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav flex-row flex-wrap bd-navbar-nav me-auto">
                  <li className="nav-item col-6 col-lg-auto">
                    <NavLink to="/home" className="nav-link" activeClassName="active" >Trang chủ</NavLink>
                  </li>
                  <li class="nav-item col-6 col-lg-auto" >
                  <NavLink to="/home" className="nav-link px-2 text-secondary" activeClassName="active">About</NavLink>
                  </li>
                  <li class="nav-item col-6 col-lg-auto" >
                    <NavLink to="/home" className="nav-link px-2 text-secondary" activeClassName="active">Blog</NavLink>
                  </li>
                  <li className="nav-item  col-6 col-lg-auto">
                    
                      <a className="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Shop</a>
                      <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                          <li><a className="dropdown-item" href="#!">Tất cả sản phẩm</a></li>
                          <li><hr className="dropdown-divider"></hr></li>
                          <li><a className="dropdown-item" href="#!">Toydi</a></li>
                          <li><a className="dropdown-item" href="#!">Rendi</a></li>
                      </ul>
                      
                  </li>
                </ul>
                <form className="d-flex">
                  <a className="btn btn-outline-dark" style={{color: 'white'}} type="submit" href="/cart">  
                      <i className="bi-cart-fill me-1" style={{color: 'white'}}></i>
                        Giỏ hàng
                      <span className="badge bg-dark text-white ms-1 rounded-pill" id="cart_quantity">0</span>
                  </a>
                </form>
              </div>
              </div>
        </nav>
      </div>
      <div className="offcanvas offcanvas-start " data-bs-scroll="true" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel" style={{width: '300px', height: '600px', backgroundColor: '#FDF4E5'}} >
          <div className="offcanvas-header ">
            <h5 className="offcanvas-title"  id="offcanvasExampleLabel">Tìm phòng</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div className="container ">
      
          </div>
      </div>
      <div style={{ backgroundColor: '#FDF4E5'}}> 
        <a href="/home" style={{padding:"10px"}}>
        <img src={'http://127.0.0.1:8000/images/logo.jpeg'} style={{  width :'50px', height:'50px'}}/>
      </a>
      </div>
      <div className="App" >
        <div className=' album py-5' style={{ backgroundColor: '#FDF4E5' }}> 
          <div className='container' > 
           
              < Route path="/home" component={ Home} />
              < Route path="/preview/:id" component={ Xemphong }/>
              
          </div>
        </div>
        
      </div>
      
      <div className=" fabPosition">
    <div className="row">
      <a style={{display: 'flex', justifyContent: 'center'}} href="https://www.instagram.com/lalendi.studio/" target="_blank">
      <img src="http://127.0.0.1:8000/images/zalo.png" className="fab2" />
      </a>
    </div>
    <div className="row ">
      <a style={{display: 'flex', justifyContent: 'center'}} href="https://www.instagram.com/lalendi.studio/" target="_blank">
      <img src="http://127.0.0.1:8000/images/logocontact.png" className="fab" />
      </a>
    </div>
    <div className="row">
      <a style={{display: 'flex', justifyContent: 'center'}} href="https://www.instagram.com/lalendi.studio/" target="_blank">
      <img src="http://127.0.0.1:8000/images/mess.png" className="fab1" />
      </a>
    </div>
      </div>
    
      <div className="container">
        <footer className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
          <div className="col-md-4 d-flex align-items-center">
            <a href="/" className="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
              <svg className="bi" width="30" height="24"></svg>
            </a>
            <span className="mb-3 mb-md-0 text-body-secondary">© 2024 LALENDI STUDIO, Inc</span>
          </div>

          <ul className="nav col-md-4 justify-content-end list-unstyled d-flex">
            <li className="ms-3"><a className="text-body-secondary" href="#"><svg className="bi" width="24" height="24"></svg></a></li>
            <li className="ms-3"><a className="text-body-secondary" href="#"><svg className="bi" width="24" height="24"></svg></a></li>
            <li className="ms-3"><a className="text-body-secondary" href="#"><svg className="bi" width="24" height="24"></svg></a></li>
          </ul>
        </footer>
      </div>
    </BrowserRouter>

  );
}

export default App;
