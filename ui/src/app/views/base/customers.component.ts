import { Component } from '@angular/core';

@Component({
  selector: 'app-customer',
  templateUrl: './customers.component.html'
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
