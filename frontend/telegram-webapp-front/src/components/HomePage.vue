<template>
  <v-container fluid>
    <h1>STONED WAY™</h1>
    <v-row justify="center"> <!-- Flex row with center alignment -->
      <v-col cols="12" md="6"> <!-- Column that takes up half the width on medium screens -->
        <v-card class="history-card">
          <v-card-title class="title-card mb-n4">History</v-card-title>
          <v-card-item>
            <v-card-subtitle>
              The History of STONED WAY™
            </v-card-subtitle>
            <v-card-text>
              A Vouched vendor for Local and Internatinal shipping. With the best sourced products available you can trust in us to privide the best Bud at the best Prices
            </v-card-text>
          </v-card-item>
        </v-card>

        <v-card class="history-card">
          <v-card-title class="title-card mb-n4">Latest Drops</v-card-title>
          <v-card-item>
            <v-card-subtitle>
              Latest STONED WAY™ Menu Updates 
            </v-card-subtitle>
            <v-row>
              <v-col cols="12" sm="6" md="4" v-for="item in menuItems" :key="item.id">
                <v-card>
                  <v-img :src="item.image" height="150" width="150" class="image-center mx-auto"></v-img>
                  <v-card-title>{{ item.name }}</v-card-title>
                  <v-card-text>${{ item.price }} lb</v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card-item>
        </v-card>
        <v-card class="history-card">
          <v-card-title class="title-card mb-n4">TouchDowns</v-card-title>
          <v-card-item>
            <v-card-subtitle>
              Join the STONED WAY™ Touchdown page
            </v-card-subtitle>
            <v-card-text>
              At STONED WAY™ we provide proof as we understand a vouch is not enough. <br/>
              Join the <a href="#">Touchdown page</a> to get the latest updates on STONED WAY™ packs.
            </v-card-text>
          </v-card-item>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template> 

<script>
import axios from 'axios';

export default {
  name: 'HomePage',
  data() {
    return {
      menuItems: [], // This will hold your menu items data
    };
  },
  created() {
    this.fetchMenuItems();
  },
  methods: {
    fetchMenuItems() {
      axios.get('http://127.0.0.1:8000/menuitems/') // Adjust the URL to your Django API endpoint
        .then(response => {
          this.menuItems = response.data;
        })
        .catch(error => {
          console.error('Error fetching menu items:', error);
        });
    }
  }
};
</script>

<style lang="css" scoped>

a {
  font-weight: bold;
  color: #9DBC98;
  text-decoration: none;
}

.image-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-center .v-image__image {
  object-fit: contain; /* Changed to 'contain' to ensure the image fits within the container */
  max-height: 100%;   /* Maximum height of the image */
  max-width: 100%;    /* Maximum width of the image */
}

.history-card {
  margin-top: 10px;
  margin-bottom: 10px;
  background-color: #84A7A1;
  color: #c9e0c6;
}

.title-card {
  padding-bottom: 0px;
}
</style>