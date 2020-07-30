<template>
  <div className="container">
    <div className="row">
      <div className="col-sm-10">
        <h1>Orders</h1>
        <hr><br><br>
          <br><br>
            <table className="table table-hover">
              <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">created_at</th>
                <th scope="col">customer_id</th>
                <th scope="col">order_name</th>
                <th></th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(order, index) in orders" :key="index">
              <td>{{order.id}}</td>
              <td>{{order.created_at}}</td>
              <td>{{order.customer_id}}</td>
              <td>{{order.order_name}}</td>
              </tr>
            </tbody>
          </table>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      orders: [],
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/orders';
      axios.get(path)
        .then((res) => {
          this.orders = res.data.orders;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
