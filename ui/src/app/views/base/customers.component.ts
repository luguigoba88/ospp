import { Component } from '@angular/core';

@Component({
  templateUrl: 'customers.component.html'
})
export class CustomersComponent {

  constructor() { }

  isCollapsed: boolean = false;

  collapsed(event: any): void {
    // console.log(event);
  }

  expanded(event: any): void {
    // console.log(event);
  }

}
