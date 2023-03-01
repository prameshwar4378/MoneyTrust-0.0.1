


  /**
   * Init swiper slider with 1 slide at once in desktop view
   */
  new Swiper('.slides-1', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });

  /**
   * Init swiper slider with 2 slides at once in desktop view
   */
  new Swiper('.slides-2', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 2,
        spaceBetween: 20
      }
    }
  });

  
document.getElementById('home-loan-section').style.display='flex';   
document.getElementById('personal-loan-section').style.display='none';      
document.getElementById('business-loan-section').style.display='none';      
document.getElementById('doctor-loan-section').style.display='none';     
document.getElementById('car-loan-section').style.display='none';      
document.getElementById('education-loan-section').style.display='none';

// Cards       
document.getElementById('cards_lifestyle_section').style.display='none';      
document.getElementById('cards_travel_and_fuel_section').style.display='none';      
document.getElementById('cards_shoping_card_section').style.display='none';      
document.getElementById('cards_reward_card_section').style.display='none';      

// Insurance       
document.getElementById('insurance_health_section').style.display='none';  



function set_range_txt_value() {
    option_value = document.getElementById("cmb_loan_type_option").value;
     
    if (option_value === "buying_a_home") {
        // Setting Calculatior Values 
        document.getElementById('home-loan-section').style.animation='fadeEffect 1s'; 

        document.getElementById('home-loan-section').style.display='flex';      
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';      
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  

        // document.getElementById("range_home_loan_amount").value=12000;
        // document.getElementById("txt_home_loan_amount").value=12000;

        // document.getElementById("range_home_loan_rate_of_interest").value=3;
        // document.getElementById("txt_home_loan_rate_of_interest").value=3;

        // document.getElementById("range_home_loan_tenure").value=3;
        // document.getElementById("txt_home_loan_tenure").value=3;

        // document.getElementById("lbl_home_loan_monthly_emi").innerHTML="Test";
        // document.getElementById("lbl_home_loan_total_interest_payable").innerHTML="Loan";
        // document.getElementById("lbl_home_loan_total_amount_payable").innerHTML="Section";



        // default tab open 
        document.getElementById("home_loan_defaultOpen").click();
    }

    else if (option_value === "buying_a_car") {
         
        document.getElementById('car-loan-section').style.animation='fadeEffect 1s'; 
     
        document.getElementById('home-loan-section').style.display='none';     
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';    
        document.getElementById('car-loan-section').style.display='flex';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  

 
        // default tab open 
        document.getElementById("car_loan_defaultOpen").click();

    }
    
    
    else if (option_value === "personal_loan") {
         
        document.getElementById('personal-loan-section').style.animation='fadeEffect 1s'; 
     
        document.getElementById('home-loan-section').style.display='none';     
        document.getElementById('personal-loan-section').style.display='flex';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';    
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  

 
        // default tab open 
        document.getElementById("personal_loan_defaultOpen").click();

    }
    
    
    else if (option_value === "business_loan") {
         
        document.getElementById('business-loan-section').style.animation='fadeEffect 1s'; 
     
        document.getElementById('home-loan-section').style.display='none';     
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='flex';      
        document.getElementById('doctor-loan-section').style.display='none';    
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  

 
        // default tab open 
        document.getElementById("business_loan_defaultOpen").click();

    }
    
    
    else if (option_value === "doctor_loan") {
         
        document.getElementById('doctor-loan-section').style.animation='fadeEffect 1s'; 
     
        document.getElementById('home-loan-section').style.display='none';   
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='flex';      
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  

 
        // default tab open 
        document.getElementById("doctor_loan_defaultOpen").click();

    }
    
    else if (option_value === "Education/Higher Studies") {

        document.getElementById('education-loan-section').style.animation='fadeEffect 1s'; 
       
        document.getElementById('home-loan-section').style.display='none';       
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';  
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='flex';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  

 
 
        // default tab open 
        document.getElementById("education_loan_defaultOpen").click();

    }
    else if (option_value === "Lifestype") {
        document.getElementById('cards_lifestyle_section').style.animation='fadeEffect 1s'; 

        document.getElementById('home-loan-section').style.display='none';     
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';    
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='flex';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  


    }
    else if (option_value === "Travel & Fuel") {
        document.getElementById('cards_travel_and_fuel_section').style.animation='fadeEffect 1s'; 

        document.getElementById('home-loan-section').style.display='none';      
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';   
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='flex';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  


    }
    else if (option_value === "Shoping") {
        document.getElementById('cards_shoping_card_section').style.animation='fadeEffect 1s'; 

        document.getElementById('home-loan-section').style.display='none';     
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';    
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='flex';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  


    }
    else if (option_value === "Rewards") {
        document.getElementById('cards_reward_card_section').style.animation='fadeEffect 1s'; 

        document.getElementById('home-loan-section').style.display='none';    
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';     
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='flex';      
        // Insurance       
        document.getElementById('insurance_health_section').style.display='none';  


    }
 

    else if (option_value === "Health Insurace"  ) { 
        
        document.getElementById('insurance_health_section').style.animation='fadeEffect 1s';  

        document.getElementById('home-loan-section').style.display='none';    
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';     
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        // Insurance       
        document.getElementById('insurance_health_section').style.display='flex';  
 
    }
    
    else if (option_value ===  "Car Insurace"  ) { 
        
        document.getElementById('insurance_health_section').style.animation='fadeEffect 1s';  

        document.getElementById('home-loan-section').style.display='none';     
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';    
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        // Insurance       
        document.getElementById('insurance_health_section').style.display='flex';  
 
    }
    
    else if (option_value ===  "Term Insurace"  ) { 
        
        document.getElementById('insurance_health_section').style.animation='fadeEffect 1s';  

        document.getElementById('home-loan-section').style.display='none';   
        document.getElementById('personal-loan-section').style.display='none';      
        document.getElementById('business-loan-section').style.display='none';      
        document.getElementById('doctor-loan-section').style.display='none';      
        document.getElementById('car-loan-section').style.display='none';      
        document.getElementById('education-loan-section').style.display='none';
        
        // Cards       
        document.getElementById('cards_lifestyle_section').style.display='none';      
        document.getElementById('cards_travel_and_fuel_section').style.display='none';      
        document.getElementById('cards_shoping_card_section').style.display='none';      
        document.getElementById('cards_reward_card_section').style.display='none';      
        // Insurance       
        document.getElementById('insurance_health_section').style.display='flex';  



    }
}






const select1 = document.getElementById("cmb_loan_type");
const select2 = document.getElementById("cmb_loan_type_option");

select1.addEventListener("change", function() {
const selectedOption = this.value;

select2.innerHTML = "";

if (selectedOption === "Loan") {
    select2.innerHTML = `
    <option value="">--- Select ---</option>
    <option value="buying_a_home">Buying a Home</option>
    <option value="buying_a_car">Buying a Car</option>
    <option value="Education/Higher Studies">Education/Higher Studies</option>
    <option value="doctor_loan">Doctor Loan</option>
    <option value="business_loan">Business Loan</option>
    <option value="personal_loan">Personal Loan</option>
    `;
} else if (selectedOption === "Cards") {
    select2.innerHTML = `
    <option value="">--- Select ---</option>
    <option value="Lifestype">Lifestype</option>
    <option value="Travel & Fuel">Travel & Fuel</option>
    <option value="Shoping">Shoping</option>
    <option value="Rewards">Rewards</option>
    `;
}
else if (selectedOption === "Insurance") {
    select2.innerHTML = `
    <option value="">--- Select ---</option>
    <option value="Health Insurace">Health Insurace</option>
    <option value="Car Insurace">Car Insurace</option>
    <option value="Term Insurace">Term Insurace</option>
    <option value="Travel Insurace">Travel Insurace</option>
    `;
}
});





const cmb_own_boss_type_select1 = document.getElementById("cmb_own_boss_type");
const cmb_own_boss_type_option_select1 = document.getElementById("cmb_own_boss_type_option");

document.getElementById('become-partner').style.display='block';
document.getElementById('hub-manager').style.display='none';

cmb_own_boss_type_select1.addEventListener("change", function() {
const selectedOption = this.value;

cmb_own_boss_type_option_select1.innerHTML = "";

if (selectedOption === "To Become Partner") {
    document.getElementById('become-partner').style.display='block';
    document.getElementById('hub-manager').style.display='none';
 cmb_own_boss_type_option_select1.innerHTML = `
    <option value="">--- Select ---</option>
    <option value="personal_loan">Higher Payout</option>
    <option value="home_loan">Timely Payout</option>
    <option value="business_loan">Availability of all Products</option>
    <option value="gold_loan">Pan India Precense</option>
    <option value="gold_loan">Money Trust Brand</option>
    <option value="gold_loan">RFSPL</option>
    `;
} else if (selectedOption === "Hub Manager") {
    document.getElementById('become-partner').style.display='none';
    document.getElementById('hub-manager').style.display='block';
 cmb_own_boss_type_option_select1.innerHTML = `
    <option value="">--- Select ---</option>
    <option value="Lifestype">Earn Best Business Pay-out(in terms of commision)</option>
    <option value="Travel & Fuel">Being a part of a promising and high-potential financial industry.</option>
    <option value="Shoping">Low Deposit or Minimum Investment</option>
    <option value="Rewards">Opportunity to establish new contacts that can be a source of life-long income</option>
    <option value="Rewards">Lucrative incentives.</option>
    <option value="Rewards">Referral Bonus</option>
    `;
}
});


   function getOption_for_calculator() {
   selectElement = document.querySelector('#cmb_loan_type_option');
   output = selectElement.value;
   // document.querySelector('.output').textContent = output;
   if (output==="personal_loan")
       { 
       document.getElementById('personal-loan-section').style.display='flex';
       document.getElementById('exception-section').style.display='none';
       document.getElementById('business-loan-section').style.display='none';
       document.getElementById('gold-loan-section').style.display='none';
       document.getElementById('home-loan-section').style.display='none';
       alert("this is sample test")
      }
   else if (output==="home_loan")      
       { 
       document.getElementById('exception-section').style.display='none';
       document.getElementById('personal-loan-section').style.display='none';
       document.getElementById('home-loan-section').style.display='flex';
       document.getElementById('business-loan-section').style.display='none';
       document.getElementById('gold-loan-section').style.display='none';
       // document.getElementById('calculator-tool').style.display='none';
       alert('Home Loan Seleted')
      }
      else if (output==="business_loan")
      {
       document.getElementById('exception-section').style.display='none';
       document.getElementById('personal-loan-section').style.display='none';
       document.getElementById('home-loan-section').style.display='none';
       document.getElementById('business-loan-section').style.display='flex';
       document.getElementById('gold-loan-section').style.display='none';
      }
      else if (output==="gold_loan")
      {
       document.getElementById('exception-section').style.display='none';
       document.getElementById('personal-loan-section').style.display='none';
       document.getElementById('home-loan-section').style.display='none';
       document.getElementById('business-loan-section').style.display='none';
       document.getElementById('gold-loan-section').style.display='flex';
      }
      else{
       document.getElementById('exception-section').style.display='flex';
       document.getElementById('personal-loan-section').style.display='none';
       document.getElementById('home-loan-section').style.display='none';
       document.getElementById('business-loan-section').style.display='none';
       document.getElementById('gold-loan-section').style.display='none';
      }
}



