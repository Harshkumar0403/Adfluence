<template>
  <div class="dashboard">
      <div class="logo">
      <img src="@/assets/logo1.png" alt="Logo" />
      <span style="font-family:Playwrite GB S;font-weight: 400">Adfluence</span>
    </div>
    <div class="header-buttons">
      
      <button @click="navigateTo('/')">Back</button>
      <button @click="logout">Logout</button>
    </div>
     <h1 style="text-align: center;font-family: 'Headland One, serif;color:#31572c">Sponsor's Dashboard</h1>
    <div class="dashboard-content">
      <div class="sidebar">
        <div class="icon-logo">
          <!-- <img src="@/assets/logo1.png" alt="Logo" class="logo" />
          <span style="font-family:Playwrite GB S;font-weight: 400">Adfluence</span> -->
        </div>
        <div class="nav-buttons">
          <button @click="showProfile">Profile</button>
          <button @click="showAddCampaign">Add Campaign</button>
          <button @click="showAdRequest">Ad Requests</button>
          <button @click="showCampaign">Campaigns</button>
          <button @click="showAd">Ads</button>
          <button @click="showInfluencers">Influencers</button>
          <button @click="showPayment">Payment</button>
          <button @click="downloadReport">Download Report</button>
        </div>
      </div>
      <div class="main-content">
        <!-- Content for the second section goes here -->
        <CaseStudyCards  v-if="defaultcard"/>
        <Profile v-if="showingProfile" />
        <AddCampaign v-if="showingAddCampaign" />
        <Campaigns  v-if="showingCampaign" />
        <Influencers v-if="showingInfluencers" />
        <!-- <AddAd v-if="showingAddAd" /> -->
        <AdComponent v-if="showingAd" />
        <AdRequests v-if="showingAdRequests" />
        <Pay v-if="showingPay" />
        <PaymentComponent v-if="showingPayment" />


      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import axios from 'axios'
import Profile from '@/components/Profile.vue';
import AddCampaign from '@/components/AddCampaign.vue';
import Footer from '@/components/Footer.vue';
import CaseStudyCards from '@/components/CaseStudyCards.vue';
import Campaigns from '@/components/Campaigns.vue';
import Influencers from '@/components/Influencers.vue';
import AddAd from '@/components/AddAd.vue';
import AdComponent from '@/components/AdComponent.vue'
import AdRequests from '@/components/AdRequests.vue';
import Pay from '@/components/Pay.vue'
import PaymentComponent from '@/components/PaymentComponent.vue'


export default {
  components: {
    Profile,
    AddCampaign,
    Footer,
    CaseStudyCards,
    Campaigns,
    Influencers,
    AdComponent,
    AdRequests,
    Pay,
    PaymentComponent
  },
  data() {
    return {
      sponsorId : localStorage.getItem('sponsor_id'),
      currentComponent: null,
      pendingAdRequests: 0, // Example, should be fetched dynamically
      showingProfile: false,
      showingAddCampaign: false,
      defaultcard :true,
      showingCampaign:false,
      showingInfluencers :false,
      showingAd:false,
      showingAdRequests : false,
      showingPay :false,
      showingPayment : false,
      

    };
  },
  methods: {
    showComponent(component) {
      this.currentComponent = component;
      console.log(this.currentComponent);
    },
    showProfile() {
      this.defaultcard = false;
      this.showingAddCampaign = false;
      this.showingProfile = true;
      this.showingCampaign=false;
      this.showingInfluencers=false;
      this.showingAd=false;
      this.showingAdRequests = false;
      this.showingPay=false;
      this.showingPayment=false;
    },
    showAdRequest(){
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingCampaign=false;
      this.showingSponsors = false;
      this.showingAdRequests = true;
       this.showingAd=false;
       this.showingAddCampaign = false;
       this.showingInfluencers=false;
       this.showingPay=true;
       this.showingPayment=false;
    },
    showAddCampaign() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingAddCampaign = true;
      this.showingCampaign=false;
      this.showingInfluencers=false;
      this.showingAd=false;
      this.showingAdRequests = false;
      this.showingPay=false;
      this.showingPayment=false;
    },
    showAd() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingAddCampaign = false;
      this.showingCampaign=false;
      this.showingInfluencers=false;
      this.showingAd=true;
      this.showingAdRequests = false;
      this.showingPay=false;
      this.showingPayment=false;
    },
    showCampaign() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingAddCampaign = false;
      this.showingCampaign=true;
      this.showingInfluencers=false;
      this.showingAd=false;
      this.showingAdRequests = false;
      this.showingPay=false;
      this.showingPayment=false;
    },
    showInfluencers() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingAddCampaign = false;
      this.showingCampaign=false;
      this.showingInfluencers=true;
      this.showingAd=false;
      this.showingAdRequests = false;
      this.showingPay=false;
      this.showingPayment=false;
    },
    showPayment() {
      this.defaultcard = false;
      this.showingProfile = false;
      this.showingAddCampaign = false;
      this.showingCampaign=false;
      this.showingInfluencers=false;
      this.showingAd=false;
      this.showingAdRequests = false;
      this.showingPay=false;
      this.showingPayment=true;
    },
    goBack() {
      this.$router.push('/');
    },
    async downloadReport() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/export-csv', {
          sponsor_id: this.sponsorId, // Pass the sponsor ID
        });
        alert('The report is being generated. You will receive an email once it is ready.');
      } catch (error) {
        console.error('Error generating report:', error);
      }
    },
    logout() {
      // Handle logout logic here
      localStorage.clear();
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.dashboard {
  background-color: #f5ebe0;
  /* height: 100vh; */
  display: flex;
  flex-direction: column;
}
.logo img {
  height: 40px;
  justify-content: flex-start;
}

.header-buttons {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
}

.header-buttons button {
  background-color: #31572c;
  color: #fff;
  border: none;
  padding: 10px;
  margin-left: 10px;
  border-radius: 18px;
  cursor: pointer;
}

.header-buttons button:hover {
  background-color: #805a4a;
}

.dashboard-content {
  display: flex;
  flex: 1;
}

.sidebar {
  width: 18vw;
  background-color: #9f7e69;
  padding: 20px;
  display: flex;
  margin-left:10px;
  flex-direction: column;
  margin-top: 25px;
  justify-content: flex-start;
  border-radius: 18px;
  height: 80 vh;
}

.nav-buttons button {
  background-color: #31572c;
  color: #fff;
  border: none;
  padding: 10px;
  margin: 10px 0;
  border-radius: 18px;
  cursor: pointer;
  width: 100%;
}

.nav-buttons button:hover {
  background-color: #ddd;
}

.main-content {
  width: 82vw;
  margin: 20px;
  padding: 20px;
  border-radius: 18px;
  background-color: white;
  height: 100vh;
  overflow: scroll;
  scrollbar-color: rgb(61, 57, 48) grey;
  scrollbar-width: thin;
}

.badge {
  background-color: red;
  color: white;
  border-radius: 50%;
  padding: 5px;
  font-size: 12px;
}

</style>